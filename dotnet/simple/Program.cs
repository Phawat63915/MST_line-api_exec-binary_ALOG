using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string accessToken = "obw4pLX4u2FpTMddsnsVh4rzwfHt04pV6netubXSZBE";
        string message = "foobar";
        await SendLineNotify(accessToken, message);
    }

    private static async Task SendLineNotify(string accessToken, string message)
    {
        string url = "https://notify-api.line.me/api/notify";

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
