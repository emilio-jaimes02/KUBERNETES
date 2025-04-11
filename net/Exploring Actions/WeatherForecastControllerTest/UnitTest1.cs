using Microsoft.Extensions.Logging;
using Moq;
using Exploring_Actions.Controllers;
using Exploring_Actions;

namespace WeatherForecastControllerTest
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            // Arrange
            var logger = new Mock<ILogger<WeatherForecastController>>();
            var controller = new WeatherForecastController(logger.Object);
            //Act
            var result = controller.Get();
            // Assert
            Assert.NotNull(result);
            Assert.IsType<WeatherForecast[]>(result);

        }
    }
}