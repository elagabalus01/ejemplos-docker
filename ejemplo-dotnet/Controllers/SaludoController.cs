using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;

namespace ejemplo.Controllers
{
    [Route("[controller]")]
    [ApiController]
    public class SaludoController:ControllerBase
    {
        [HttpGet]
        public ActionResult<string> getSaludo()
        {

            return Ok("Hola mundo");
        }
    }
}