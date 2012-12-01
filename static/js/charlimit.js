function CharLimit(input){
    this.maxChars = 140;
    this.$charDisplay = $('#remaining-chars');
    this.updateRemainingChars(this.maxChars);

    input.keydown(function(e){
	var remaining = $(e.target).val().length;
	this.updateRemainingChars(this.maxChars - remaining);
    }.bind(this));
}

CharLimit.prototype.updateRemainingChars = function(num){
    if (num > this.maxChars / 2){
	this.$charDisplay.removeClass('bad ugly').addClass('good');
    }
    else if (num <= 20 && num > 0){
	this.$charDisplay.removeClass('ugly good').addClass('bad');
    }
    else if (num < 0){
	this.$charDisplay.removeClass('good bad').addClass('ugly');
    }
    this.$charDisplay.html(num);
};
