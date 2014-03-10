from django import forms
from readlikeme.app.reader.models import Article


class ArticleForm(forms.ModelForm):
	url = forms.URLField(widget=forms.widgets.Textarea(attrs={'placeholder': 'http://the.website/the-article'}), required=True)

	def is_valid(self):
		form = super(ArticleForm, self).is_valid()
		for f in self.errors.iterkeys():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'placeholder': 'Wrong URL...'})

	class Meta:
		model = Article
		exlude = ('user',)