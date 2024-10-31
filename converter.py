from flask import Flask, render_template, request
#change test
def convert_to_decimal(num, base):
    num = list(num)[::-1]
    ans = 0
    base = int(base)
    for i in range(len(num)):
        if num[i] == 'A':
            ans += 10 * base**i
        elif num[i] == 'B':
            ans += 11 * base**i
        elif num[i] == 'C':
            ans += 12 * base**i
        elif num[i] == 'D':
            ans += 13 * base**i
        elif num[i] == 'E':
            ans += 14 * base**i
        elif num[i] == 'F':
            ans += 15 * base**i
        else:
            ans += int(num[i]) * base**i

    return ans


def convert_to_any_base(num, base):
    ans = ''
    num = int(num)
    base = int(base)
    while num > 0:
        if num % base == 10:
            ans += 'A'
        elif num % base == 11:
            ans += 'B'
        elif num % base == 12:
            ans += 'C'
        elif num % base == 13:
            ans += 'D'
        elif num % base == 14:
            ans += 'E'
        elif num % base == 15:
            ans += 'F'
        else:
            ans += str(num % base)
        num //= base
    return ans[::-1]

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':

        num_dec = request.form['num_dec']
        num_base = request.form['num_base']
        base = request.form['base']

        if num_dec == '':
            num_dec = convert_to_decimal(num_base, base)
        else:
            num_base = convert_to_any_base(num_dec, base)
            
        return render_template('index.html', num_dec = num_dec, num_base = num_base, base = base)

        
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug= True)

