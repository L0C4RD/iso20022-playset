from . import base_types
from ._Max35Text import Max35Text
from ._Max3NumericText import Max3NumericText
from ._PaymentInstrument1Code import PaymentInstrument1Code

class PaymentOrigin1Choice(base_types._BaseFieldType):

	__slots__ = ["_FINMT", "_Instrm", "_Prtry", "_XMLMsgNm"]
	@property
	def FINMT(self):
		return self._FINMT

	@FINMT.setter
	def FINMT(self, value):
		self._FINMT = value if type(value) != base_types.auto else self.make_default("FINMT")

	@FINMT.deleter
	def FINMT(self):
		del self._FINMT
		self._FINMT = None

	@property
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if type(value) != base_types.auto else self.make_default("Instrm")

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def XMLMsgNm(self):
		return self._XMLMsgNm

	@XMLMsgNm.setter
	def XMLMsgNm(self, value):
		self._XMLMsgNm = value if type(value) != base_types.auto else self.make_default("XMLMsgNm")

	@XMLMsgNm.deleter
	def XMLMsgNm(self):
		del self._XMLMsgNm
		self._XMLMsgNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FINMT', type=Max3NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Instrm', type=PaymentInstrument1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XMLMsgNm', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

