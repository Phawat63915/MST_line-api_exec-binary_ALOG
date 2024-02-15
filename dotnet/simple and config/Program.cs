using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using CommandLine;
using Microsoft.Extensions.Configuration;

class Options
{
    [Option('m', "message", Required = true, HelpText = "Message to send.")]
    public string? Message { get; set; }
}

class Program
{
    static async Task Main(string[] args)
    {
        IConfiguration config = new ConfigurationBuilder()
            .AddTomlFile("config.toml")
            .Build();
        string? accessToken = config["line:access_token"];
        string? notifyUrl = config["line:notify_url"];

        if (accessToken == null || notifyUrl == null)
        {
            Console.WriteLine("Error: access_token or notify_url is missing in config.toml.");
            return;
        }

        await Parser.Default.ParseArguments<Options>(args)
            // .WithParsedAsync(async options => await SendLineNotify(accessToken, notifyUrl, options.Message));
            .WithParsedAsync(async options => await SendLineNotify(accessToken, notifyUrl, options.Message!));
            
        // await Parser.Default.ParseArguments<Options>(args) // Error CS8625: Cannot convert null literal to non-nullable reference type.
        //     .WithParsedAsync(async options =>
        //     {
        //         if (options.Message != null)
        //         {
        //             await SendLineNotify(accessToken, notifyUrl, options.Message);
        //         }
        //         else
        //         {
        //             Console.WriteLine("Error: Message is null.");
        //         }
        //     });
    }

    private static async Task SendLineNotify(string accessToken, string url, string message)
    {
        using var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", accessToken);

        var content = new MultipartFormDataContent
        {
            { new StringContent(message), "message" }
        };

        HttpResponseMessage response = await httpClient.PostAsync(url, content);

        Console.WriteLine(response.StatusCode);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
