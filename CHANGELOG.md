# Change Log

## [1.0.7] 2023-08-14
### Changes

- Fix #10, collectstatic bumps errors
- Remove `ASSETS_ROOT` variable
- Added `Render` Support (CI/CD)

## [1.0.6] 2022-09-05
### Improvements

- Improved Authentication
  - Visual password strength indicator (registration)  
  - **Social Login**: `Github` & `Twitter`
- New Feature: `User Profiles`
  - `Extended User` profile
  - `Self-Deletion` option
- Improved `Docker` Scripts   

## [1.0.5] 2022-08-29
### Improvements

- Refactoring User Dashboard
  - `dashboard-settings.html` 
  - `dashboard-security.html`

## [1.0.4] 2022-06-13
### Improvements

- Built with [Pixel Pro Generator](https://appseed.us/generator/pixel-bootstrap-pro/)
  - Timestamp: `2022-06-13 20:10`

## [1.0.3] 2021-09-10
### Improvements & Fixes

- Bump Django Codebase to [v1.0.5](https://github.com/app-generator/boilerplate-code-django/releases)
  - Dependencies update (all packages)
  - Use Django==3.2.6 (latest stable version)
  - Better Code formatting
  - Improved Files organization
  - Optimize imports
  - Docker Scripts Update 
- Fixes: 
  - Patch 500 Error when authenticated users access `admin` path (no slash at the end)
  - Patch [#16](https://github.com/app-generator/boilerplate-code-django-dashboard/issues/16): Minor issue in Docker 

## [1.0.2] 2021-07-01

- Bump UI: Pixel Pro Bootstrap 5 - v5.4.0
- Added scripts to recompile SCSS
    - `app/static/assets`: Gulp toolchain

## [1.0.1] 2021-01-23
### Improvements

- UI: [Jinja Pixel PRO](https://github.com/app-generator/jinja-pixel-pro/releases) v1.0.1 
- Pixel Pro Bootstrap 5 - v5.2.0
- Codebase: [Django Boilerplate](https://github.com/app-generator/boilerplate-code-django/releases) - v1.0.4

## [1.0.0] 2020-02-07
### Initial Release
