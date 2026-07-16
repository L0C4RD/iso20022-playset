# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositiveNumber
from . import ServiceResponse10

class ReportTransactionResponse8(base_types._BaseFieldType):

	__slots__ = ["_BlckStart", "_BlckStop", "_RptFullSz", "_TxRpt"]
	@property
	def BlckStart(self):
		return self._BlckStart

	@BlckStart.setter
	def BlckStart(self, value):
		self._BlckStart = value if value is not None else base_types.UninitialisedField(self, 'BlckStart', PositiveNumber, False)

	@BlckStart.deleter
	def BlckStart(self):
		del self._BlckStart
		self._BlckStart = base_types.UninitialisedField(self, 'BlckStart', PositiveNumber, False)

	@property
	def BlckStop(self):
		return self._BlckStop

	@BlckStop.setter
	def BlckStop(self, value):
		self._BlckStop = value if value is not None else base_types.UninitialisedField(self, 'BlckStop', PositiveNumber, False)

	@BlckStop.deleter
	def BlckStop(self):
		del self._BlckStop
		self._BlckStop = base_types.UninitialisedField(self, 'BlckStop', PositiveNumber, False)

	@property
	def RptFullSz(self):
		return self._RptFullSz

	@RptFullSz.setter
	def RptFullSz(self, value):
		self._RptFullSz = value if value is not None else base_types.UninitialisedField(self, 'RptFullSz', PositiveNumber, False)

	@RptFullSz.deleter
	def RptFullSz(self):
		del self._RptFullSz
		self._RptFullSz = base_types.UninitialisedField(self, 'RptFullSz', PositiveNumber, False)

	@property
	def TxRpt(self):
		return self._TxRpt

	@TxRpt.setter
	def TxRpt(self, value):
		self._TxRpt = value if value is not None else base_types.UninitialisedField(self, 'TxRpt', ServiceResponse10, True)

	@TxRpt.deleter
	def TxRpt(self):
		del self._TxRpt
		self._TxRpt = base_types.UninitialisedField(self, 'TxRpt', ServiceResponse10, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckStart', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckStop', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptFullSz', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRpt', type=ServiceResponse10, min=0, max=None, mutex_group=None, array=True),
	))