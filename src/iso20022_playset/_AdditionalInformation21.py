# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max20KText
from . import OutputFormat4Code
from . import PartyType23Code
from . import UserInterface7Code

class AdditionalInformation21(base_types._BaseFieldType):

	__slots__ = ["_Frmt", "_Rcpt", "_Trgt", "_Val"]
	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', OutputFormat4Code, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', OutputFormat4Code, False)

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', PartyType23Code, False)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', PartyType23Code, False)

	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if value is not None else base_types.UninitialisedField(self, 'Trgt', UserInterface7Code, True)

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = base_types.UninitialisedField(self, 'Trgt', UserInterface7Code, True)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max20KText, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max20KText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frmt', type=OutputFormat4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=PartyType23Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trgt', type=UserInterface7Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Val', type=Max20KText, min=1, max=1, mutex_group=None, array=False),
	))