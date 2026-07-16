# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification242Choice
from . import UniqueTransactionIdentifier3

class TradingSideTransactionReporting3(base_types._BaseFieldType):

	__slots__ = ["_RptgJursdctn", "_RptgPty", "_TradgSdUnqTxIdr"]
	@property
	def RptgJursdctn(self):
		return self._RptgJursdctn

	@RptgJursdctn.setter
	def RptgJursdctn(self, value):
		self._RptgJursdctn = value if value is not None else base_types.UninitialisedField(self, 'RptgJursdctn', Max35Text, False)

	@RptgJursdctn.deleter
	def RptgJursdctn(self):
		del self._RptgJursdctn
		self._RptgJursdctn = base_types.UninitialisedField(self, 'RptgJursdctn', Max35Text, False)

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if value is not None else base_types.UninitialisedField(self, 'RptgPty', PartyIdentification242Choice, False)

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = base_types.UninitialisedField(self, 'RptgPty', PartyIdentification242Choice, False)

	@property
	def TradgSdUnqTxIdr(self):
		return self._TradgSdUnqTxIdr

	@TradgSdUnqTxIdr.setter
	def TradgSdUnqTxIdr(self, value):
		self._TradgSdUnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'TradgSdUnqTxIdr', UniqueTransactionIdentifier3, True)

	@TradgSdUnqTxIdr.deleter
	def TradgSdUnqTxIdr(self):
		del self._TradgSdUnqTxIdr
		self._TradgSdUnqTxIdr = base_types.UninitialisedField(self, 'TradgSdUnqTxIdr', UniqueTransactionIdentifier3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgJursdctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdUnqTxIdr', type=UniqueTransactionIdentifier3, min=0, max=None, mutex_group=None, array=True),
	))