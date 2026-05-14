# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max20KText import Max20KText
from ._OutputFormat4Code import OutputFormat4Code
from ._PartyType23Code import PartyType23Code
from ._UserInterface7Code import UserInterface7Code

class AdditionalInformation21(base_types._BaseFieldType):

	__slots__ = ["_Frmt", "_Rcpt", "_Trgt", "_Val"]
	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if type(value) != base_types.auto else self.make_default("Rcpt")

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = None

	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if type(value) != base_types.auto else self.make_default("Trgt")

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frmt', type=OutputFormat4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=PartyType23Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trgt', type=UserInterface7Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Val', type=Max20KText, min=1, max=1, mutex_group=None, array=False),
	))