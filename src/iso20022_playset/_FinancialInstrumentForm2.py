# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Appearance3Choice
from . import FormOfSecurity8Choice

class FinancialInstrumentForm2(base_types._BaseFieldType):

	__slots__ = ["_BookgApprnc", "_LglForm"]
	@property
	def BookgApprnc(self):
		return self._BookgApprnc

	@BookgApprnc.setter
	def BookgApprnc(self, value):
		self._BookgApprnc = value if value is not None else base_types.UninitialisedField(self, 'BookgApprnc', Appearance3Choice, False)

	@BookgApprnc.deleter
	def BookgApprnc(self):
		del self._BookgApprnc
		self._BookgApprnc = base_types.UninitialisedField(self, 'BookgApprnc', Appearance3Choice, False)

	@property
	def LglForm(self):
		return self._LglForm

	@LglForm.setter
	def LglForm(self, value):
		self._LglForm = value if value is not None else base_types.UninitialisedField(self, 'LglForm', FormOfSecurity8Choice, False)

	@LglForm.deleter
	def LglForm(self):
		del self._LglForm
		self._LglForm = base_types.UninitialisedField(self, 'LglForm', FormOfSecurity8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BookgApprnc', type=Appearance3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglForm', type=FormOfSecurity8Choice, min=0, max=1, mutex_group=None, array=False),
	))