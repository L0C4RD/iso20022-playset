# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._PartyIdentification242Choice import PartyIdentification242Choice
from ._UniqueTransactionIdentifier3 import UniqueTransactionIdentifier3

class CounterpartySideTransactionReporting3(base_types._BaseFieldType):

	__slots__ = ["_CtrPtySdUnqTxIdr", "_RptgJursdctn", "_RptgPty"]
	@property
	def CtrPtySdUnqTxIdr(self):
		return self._CtrPtySdUnqTxIdr

	@CtrPtySdUnqTxIdr.setter
	def CtrPtySdUnqTxIdr(self, value):
		self._CtrPtySdUnqTxIdr = value if type(value) != base_types.auto else self.make_default("CtrPtySdUnqTxIdr")

	@CtrPtySdUnqTxIdr.deleter
	def CtrPtySdUnqTxIdr(self):
		del self._CtrPtySdUnqTxIdr
		self._CtrPtySdUnqTxIdr = None

	@property
	def RptgJursdctn(self):
		return self._RptgJursdctn

	@RptgJursdctn.setter
	def RptgJursdctn(self, value):
		self._RptgJursdctn = value if type(value) != base_types.auto else self.make_default("RptgJursdctn")

	@RptgJursdctn.deleter
	def RptgJursdctn(self):
		del self._RptgJursdctn
		self._RptgJursdctn = None

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if type(value) != base_types.auto else self.make_default("RptgPty")

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtySdUnqTxIdr', type=UniqueTransactionIdentifier3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgJursdctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
	))