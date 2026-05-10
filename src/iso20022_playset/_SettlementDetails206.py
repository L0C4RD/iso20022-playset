from . import base_types
from ._CollateralOwnership4 import CollateralOwnership4
from ._ISODateTime import ISODateTime
from ._SettlementParties36Choice import SettlementParties36Choice

class SettlementDetails206(base_types._BaseFieldType):

	__slots__ = ["_CollOwnrsh", "_SttlmPties", "_TradDt"]
	@property
	def CollOwnrsh(self):
		return self._CollOwnrsh

	@CollOwnrsh.setter
	def CollOwnrsh(self, value):
		self._CollOwnrsh = value if type(value) != base_types.auto else self.make_default("CollOwnrsh")

	@CollOwnrsh.deleter
	def CollOwnrsh(self):
		del self._CollOwnrsh
		self._CollOwnrsh = None

	@property
	def SttlmPties(self):
		return self._SttlmPties

	@SttlmPties.setter
	def SttlmPties(self, value):
		self._SttlmPties = value if type(value) != base_types.auto else self.make_default("SttlmPties")

	@SttlmPties.deleter
	def SttlmPties(self):
		del self._SttlmPties
		self._SttlmPties = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollOwnrsh', type=CollateralOwnership4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPties', type=SettlementParties36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

