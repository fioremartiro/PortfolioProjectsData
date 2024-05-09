/*
Covid 19 Data Exploration 

Skills used: Joins, CTE's, Temp Tables, Windows Functions, Aggregate Functions, Creating Views, Converting Data Types

*/

Select *
From PortfolioProject..CovidDeaths
Where continent is not null 
order by 3,4

-- Select Data that we are going to be starting with

SELECT location, date, total_cases, new_cases,  total_deaths, population
FROM PortfolioProject..CovidDeaths
Where continent is not null 
Order by 1,2

-- Total Cases vs Total Deaths
-- Shows likelihood of dying if you contract covid in your country

SELECT location, date, total_cases, total_deaths,
       CAST(total_deaths AS DECIMAL) / CAST(total_cases AS DECIMAL)*100 as DeathPercentage
FROM PortfolioProject..CovidDeaths
WHERE location like '%states%'
and continent is not null 
ORDER BY 1,2

-- Total Cases vs Population
-- Shows what percentage of population infected with Covid

SELECT location, date, population, total_cases,
       (CAST(total_cases AS DECIMAL) / CAST(population AS DECIMAL)) * 100 AS PercentPopulationInfected
FROM PortfolioProject..CovidDeaths
--WHERE location LIKE '%States%'
Where continent is not null 
ORDER BY 1,2

-- Countries with Highest Infection Rate compared to Population

SELECT location, population, 
       MAX(total_cases) AS HighestTotalCases,
       MAX(CAST(total_cases AS DECIMAL) / CAST(population AS DECIMAL)) * 100 AS PercentPopulationInfected
FROM PortfolioProject..CovidDeaths
--WHERE location LIKE '%States%'
Where continent is not null 
GROUP BY location, population
ORDER BY PercentPopulationInfected DESC; -- Ordering by the infection rate in descending order for clarity

-- Countries with Highest Death Count per Population

SELECT location, MAX(CAST(total_deaths as int)) as TotalDeathCount
FROM PortfolioProject..CovidDeaths
--WHERE location LIKE '%States%'
Where continent is not null 
GROUP BY location
ORDER BY TotalDeathCount DESC; -- Ordering by the infection rate in descending order for clarity

-- BREAKING THINGS DOWN BY CONTINENT

-- Showing contintents with the highest death count per population

SELECT continent, MAX(CAST(total_deaths as int)) as TotalDeathCount
FROM PortfolioProject..CovidDeaths
--WHERE location LIKE '%States%'
Where continent is not null 
GROUP BY continent
ORDER BY TotalDeathCount DESC;


-- GLOBAL NUMBERS

SELECT 
	date, 
	SUM(new_cases) AS TotalNewCases,
	SUM(CAST(new_deaths as int)) AS TotalNewDeaths,
	CASE 
        WHEN SUM(new_cases) = 0 THEN 0 -- Avoid division by zero
        ELSE SUM(CAST(new_deaths AS DECIMAL)) / SUM(CAST(new_cases AS DECIMAL)) * 100 
    END AS DeathPercentage
FROM PortfolioProject..CovidDeaths
WHERE continent is not null 
GROUP BY date
ORDER BY 1,2

-- Total Population vs Vaccinations
-- Shows Percentage of Population that has recieved at least one Covid Vaccine
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, 
    SUM(CAST(vac.new_vaccinations as bigint)) OVER (PARTITION BY dea.location ORDER BY dea.date) AS RollingPeopleVaccinated
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
    ON dea.location = vac.location
    AND dea.date = vac.date
WHERE dea.continent is not null
ORDER BY dea.location, dea.date;

-- Using CTE to perform Calculation on Partition By in previous query

WITH PopvsVac AS ( -- The WITH clause defines a temporary named result set 'PopvsVac'.
    SELECT 
        dea.continent, 
        dea.location, 
        dea.date, 
        dea.population, 
        vac.new_vaccinations, 
        SUM(CAST(vac.new_vaccinations AS bigint)) OVER (PARTITION BY dea.location ORDER BY dea.date) AS RollingPeopleVaccinated -- 'RollingPeopleVaccinated' calculates the cumulative total of vaccinations by location, ordered by date.
    FROM PortfolioProject..CovidDeaths dea
    JOIN PortfolioProject..CovidVaccinations vac
        ON dea.location = vac.location
        AND dea.date = vac.date
    WHERE dea.continent IS NOT NULL
)
SELECT *, (RollingPeopleVaccinated/population)*100 AS Calculation -- Percentage of the population that has been vaccinated up to each date.
FROM PopvsVac
ORDER BY location, date;

-- Using Temp Table to perform Calculation on Partition By in previous query
-- Dropping the temporary table if it exists

DROP TABLE IF EXISTS #PercentPopulationVaccinated;

-- Creating the temporary table
CREATE TABLE #PercentPopulationVaccinated
(
    Continent NVARCHAR(255),
    Location NVARCHAR(255),
    Date DATETIME,
    Population NUMERIC,
    New_vaccinations NUMERIC,
    RollingPeopleVaccinated NUMERIC
);

-- Inserting data into the temporary table
INSERT INTO #PercentPopulationVaccinated
SELECT 
    dea.continent, 
    dea.location, 
    dea.date, 
    dea.population, 
    vac.new_vaccinations,
    SUM(CONVERT(BIGINT, vac.new_vaccinations)) OVER (
        PARTITION BY dea.location 
        ORDER BY dea.date
    ) AS RollingPeopleVaccinated
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
    ON dea.location = vac.location
    AND dea.date = vac.date
WHERE dea.continent IS NOT NULL;

-- Selecting data and performing calculations
SELECT *,
    (RollingPeopleVaccinated / Population) * 100 AS PercentageVaccinated
FROM #PercentPopulationVaccinated
ORDER BY Location, Date;

-- Creating View to store data for later visualizations

USE PortfolioProject;
GO

IF OBJECT_ID('dbo.PercentPopulationVaccinated', 'V') IS NOT NULL
    DROP VIEW dbo.PercentPopulationVaccinated;
GO

CREATE VIEW dbo.PercentPopulationVaccinated AS
SELECT
    dea.continent,
    dea.location,
    dea.date,
    dea.population,
    vac.new_vaccinations,
    SUM(CONVERT(INT, vac.new_vaccinations)) OVER (
        PARTITION BY dea.location 
        ORDER BY dea.date) AS RollingPeopleVaccinated
FROM dbo.CovidDeaths dea
JOIN dbo.CovidVaccinations vac
    ON dea.location = vac.location
    AND dea.date = vac.date
WHERE dea.continent IS NOT NULL;