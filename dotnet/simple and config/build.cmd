rd /s /q bin
dotnet publish -c Release -r win-x86 --self-contained true /p:PublishSingleFile=true /p:IncludeNativeLibrariesForSelfExtract=true /p:DebugType=None

copy config.toml bin\Release\net7.0\win-x86\publish\config.toml
@REM dotnet publish -c Release -r win-x64 --self-contained true /p:PublishSingleFile=true /p:IncludeNativeLibrariesForSelfExtract=true /p:DebugType=None


@REM dotnet publish -c Release -r win-x64 --self-contained