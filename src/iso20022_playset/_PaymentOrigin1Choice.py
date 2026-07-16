# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Max3NumericText
from . import PaymentInstrument1Code

class PaymentOrigin1Choice(base_types._BaseFieldType):

	__slots__ = ["_FINMT", "_Instrm", "_Prtry", "_XMLMsgNm"]
	@property
	def FINMT(self):
		return self._FINMT

	@FINMT.setter
	def FINMT(self, value):
		self._FINMT = value if value is not None else base_types.UninitialisedField(self, 'FINMT', Max3NumericText, False)

	@FINMT.deleter
	def FINMT(self):
		del self._FINMT
		self._FINMT = base_types.UninitialisedField(self, 'FINMT', Max3NumericText, False)

	@property
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if value is not None else base_types.UninitialisedField(self, 'Instrm', PaymentInstrument1Code, False)

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = base_types.UninitialisedField(self, 'Instrm', PaymentInstrument1Code, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', Max35Text, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', Max35Text, False)

	@property
	def XMLMsgNm(self):
		return self._XMLMsgNm

	@XMLMsgNm.setter
	def XMLMsgNm(self, value):
		self._XMLMsgNm = value if value is not None else base_types.UninitialisedField(self, 'XMLMsgNm', Max35Text, False)

	@XMLMsgNm.deleter
	def XMLMsgNm(self):
		del self._XMLMsgNm
		self._XMLMsgNm = base_types.UninitialisedField(self, 'XMLMsgNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FINMT', type=Max3NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Instrm', type=PaymentInstrument1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XMLMsgNm', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))