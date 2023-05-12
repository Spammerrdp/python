from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return """<style>#k{color:grey;} #k1{color:#1a2421;background-color:#cbcbcb;font-size: 20px;text-align:bottom;height:40px;width:30px}</style>
    <form method="POST" action="/calculate">
    <table border="10">
        <tr>
          <td>
              <input type="text" id="display" name = "cal" style="font-size: 20px; font-align: center;height:40px;width:130px;">
  <br>
          </td>
        </tr>
        <tr>
            <td>
      <input type="button" value="1" id="k1" onclick="updateDisplay('1')">
      <input type="button" value="2"  id="k1" onclick="updateDisplay('2')">
      <input type="button" value="3"  id="k1" onclick="updateDisplay('3')">
      <input type="button" value="4"  id="k1" onclick="updateDisplay('4')">
          </td></tr>
        <tr>
            <td>
      <input type="button" value="5" id="k1" onclick="updateDisplay('5')">
      <input type="button" value="6"  id="k1" onclick="updateDisplay('6')">
      <input type="button" value="7"  id="k1" onclick="updateDisplay('7')">
      <input type="button" value="8"  id="k1" onclick="updateDisplay('8')">
          </td></tr>
        <tr>
            <td>
      <input type="button" value="9" id="k1" onclick="updateDisplay('9')">
      <input type="button" value="0"  id="k1" onclick="updateDisplay('0')">
      <input type="button" value="-"  id="k1" onclick="updateDisplay('-')">
      <input type="button" value="*"  id="k1" onclick="updateDisplay('*')">
          </td></tr>
        <tr>
            <td>
      <input type="button" value="+" id="k1" onclick="updateDisplay('+')">
      <input type="button" value="/"  id="k1" onclick="updateDisplay('/')">
      <input type="submit" id="k1" value="=">
                <input type="button" value="C"  id="k1" onclick="deletee('')">
          </td></tr></table>
</form>

<script>
function updateDisplay(value) {
  var display = document.getElementById('display');
  display.value += value;
}
function deletee() {
var display = document.getElementById('display');
  display.value = display.value.slice(0, -1);
}
</script>


    """
@app.route("/calculate", methods=["POST"])
def calculate():
    oper = str(request.form['cal'])
    result = str(eval(oper))
    return result
if __name__ == '__main__':
    app.run(debug=True,port=7007)
