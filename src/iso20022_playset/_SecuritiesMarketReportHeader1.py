# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Period4Choice
from . import TradingVenueIdentification1Choice

class SecuritiesMarketReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_RptgNtty", "_RptgPrd", "_SubmissnDtTm"]
	@property
	def RptgNtty(self):
		return self._RptgNtty

	@RptgNtty.setter
	def RptgNtty(self, value):
		self._RptgNtty = value if value is not None else base_types.UninitialisedField(self, 'RptgNtty', TradingVenueIdentification1Choice, False)

	@RptgNtty.deleter
	def RptgNtty(self):
		del self._RptgNtty
		self._RptgNtty = base_types.UninitialisedField(self, 'RptgNtty', TradingVenueIdentification1Choice, False)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@property
	def SubmissnDtTm(self):
		return self._SubmissnDtTm

	@SubmissnDtTm.setter
	def SubmissnDtTm(self, value):
		self._SubmissnDtTm = value if value is not None else base_types.UninitialisedField(self, 'SubmissnDtTm', ISODateTime, False)

	@SubmissnDtTm.deleter
	def SubmissnDtTm(self):
		del self._SubmissnDtTm
		self._SubmissnDtTm = base_types.UninitialisedField(self, 'SubmissnDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgNtty', type=TradingVenueIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))