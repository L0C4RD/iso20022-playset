from . import base_types
from ._EncryptedData2 import EncryptedData2
from ._Max10MbText import Max10MbText
from ._Max10NumericText import Max10NumericText
from ._Max20MbBinary import Max20MbBinary

class ReportContent3(base_types._BaseFieldType):

	__slots__ = ["_Binry", "_PrtctdData", "_RptLineSeq", "_Txt"]
	@property
	def Binry(self):
		return self._Binry

	@Binry.setter
	def Binry(self, value):
		self._Binry = value if type(value) != base_types.auto else self.make_default("Binry")

	@Binry.deleter
	def Binry(self):
		del self._Binry
		self._Binry = None

	@property
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if type(value) != base_types.auto else self.make_default("PrtctdData")

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = None

	@property
	def RptLineSeq(self):
		return self._RptLineSeq

	@RptLineSeq.setter
	def RptLineSeq(self, value):
		self._RptLineSeq = value if type(value) != base_types.auto else self.make_default("RptLineSeq")

	@RptLineSeq.deleter
	def RptLineSeq(self):
		del self._RptLineSeq
		self._RptLineSeq = None

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if type(value) != base_types.auto else self.make_default("Txt")

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Binry', type=Max20MbBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=EncryptedData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptLineSeq', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txt', type=Max10MbText, min=0, max=1, mutex_group=None, array=False),
	))

