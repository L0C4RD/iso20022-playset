# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InternalisationData1

class SettlementInternaliserTransactionType1(base_types._BaseFieldType):

	__slots__ = ["_CollMgmtOpr", "_OthrTxs", "_RpAgrmt", "_SctiesBuyOrSell", "_SctiesLndgOrBrrwg"]
	@property
	def CollMgmtOpr(self):
		return self._CollMgmtOpr

	@CollMgmtOpr.setter
	def CollMgmtOpr(self, value):
		self._CollMgmtOpr = value if value is not None else base_types.UninitialisedField(self, 'CollMgmtOpr', InternalisationData1, False)

	@CollMgmtOpr.deleter
	def CollMgmtOpr(self):
		del self._CollMgmtOpr
		self._CollMgmtOpr = base_types.UninitialisedField(self, 'CollMgmtOpr', InternalisationData1, False)

	@property
	def OthrTxs(self):
		return self._OthrTxs

	@OthrTxs.setter
	def OthrTxs(self, value):
		self._OthrTxs = value if value is not None else base_types.UninitialisedField(self, 'OthrTxs', InternalisationData1, False)

	@OthrTxs.deleter
	def OthrTxs(self):
		del self._OthrTxs
		self._OthrTxs = base_types.UninitialisedField(self, 'OthrTxs', InternalisationData1, False)

	@property
	def RpAgrmt(self):
		return self._RpAgrmt

	@RpAgrmt.setter
	def RpAgrmt(self, value):
		self._RpAgrmt = value if value is not None else base_types.UninitialisedField(self, 'RpAgrmt', InternalisationData1, False)

	@RpAgrmt.deleter
	def RpAgrmt(self):
		del self._RpAgrmt
		self._RpAgrmt = base_types.UninitialisedField(self, 'RpAgrmt', InternalisationData1, False)

	@property
	def SctiesBuyOrSell(self):
		return self._SctiesBuyOrSell

	@SctiesBuyOrSell.setter
	def SctiesBuyOrSell(self, value):
		self._SctiesBuyOrSell = value if value is not None else base_types.UninitialisedField(self, 'SctiesBuyOrSell', InternalisationData1, False)

	@SctiesBuyOrSell.deleter
	def SctiesBuyOrSell(self):
		del self._SctiesBuyOrSell
		self._SctiesBuyOrSell = base_types.UninitialisedField(self, 'SctiesBuyOrSell', InternalisationData1, False)

	@property
	def SctiesLndgOrBrrwg(self):
		return self._SctiesLndgOrBrrwg

	@SctiesLndgOrBrrwg.setter
	def SctiesLndgOrBrrwg(self, value):
		self._SctiesLndgOrBrrwg = value if value is not None else base_types.UninitialisedField(self, 'SctiesLndgOrBrrwg', InternalisationData1, False)

	@SctiesLndgOrBrrwg.deleter
	def SctiesLndgOrBrrwg(self):
		del self._SctiesLndgOrBrrwg
		self._SctiesLndgOrBrrwg = base_types.UninitialisedField(self, 'SctiesLndgOrBrrwg', InternalisationData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollMgmtOpr', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTxs', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpAgrmt', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesBuyOrSell', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesLndgOrBrrwg', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
	))