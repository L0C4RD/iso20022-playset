from . import base_types
from ._PositiveNumber import PositiveNumber
from ._ServiceResponse9 import ServiceResponse9

class ReportTransactionResponse7(base_types._BaseFieldType):

	__slots__ = ["_BlckStart", "_BlckStop", "_RptFullSz", "_TxRpt"]
	@property
	def BlckStart(self):
		return self._BlckStart

	@BlckStart.setter
	def BlckStart(self, value):
		self._BlckStart = value if type(value) != base_types.auto else self.make_default("BlckStart")

	@BlckStart.deleter
	def BlckStart(self):
		del self._BlckStart
		self._BlckStart = None

	@property
	def BlckStop(self):
		return self._BlckStop

	@BlckStop.setter
	def BlckStop(self, value):
		self._BlckStop = value if type(value) != base_types.auto else self.make_default("BlckStop")

	@BlckStop.deleter
	def BlckStop(self):
		del self._BlckStop
		self._BlckStop = None

	@property
	def RptFullSz(self):
		return self._RptFullSz

	@RptFullSz.setter
	def RptFullSz(self, value):
		self._RptFullSz = value if type(value) != base_types.auto else self.make_default("RptFullSz")

	@RptFullSz.deleter
	def RptFullSz(self):
		del self._RptFullSz
		self._RptFullSz = None

	@property
	def TxRpt(self):
		return self._TxRpt

	@TxRpt.setter
	def TxRpt(self, value):
		self._TxRpt = value if type(value) != base_types.auto else self.make_default("TxRpt")

	@TxRpt.deleter
	def TxRpt(self):
		del self._TxRpt
		self._TxRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckStart', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckStop', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptFullSz', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRpt', type=ServiceResponse9, min=0, max=None, mutex_group=None, array=True),
	))

