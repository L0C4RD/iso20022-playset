# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CaseStatus2Code
from . import ISODateTime
from . import Max140Text

class CaseStatus2(base_types._BaseFieldType):

	__slots__ = ["_CaseSts", "_DtTm", "_Rsn"]
	@property
	def CaseSts(self):
		return self._CaseSts

	@CaseSts.setter
	def CaseSts(self, value):
		self._CaseSts = value if value is not None else base_types.UninitialisedField(self, 'CaseSts', CaseStatus2Code, False)

	@CaseSts.deleter
	def CaseSts(self):
		del self._CaseSts
		self._CaseSts = base_types.UninitialisedField(self, 'CaseSts', CaseStatus2Code, False)

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if value is not None else base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max140Text, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CaseSts', type=CaseStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))