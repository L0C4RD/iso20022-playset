# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet5
from . import CollateralAccount3
from . import CollateralValuation13
from . import Summary3

class Collateral53(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_BlckChainAdrOrWllt", "_CollValtn", "_RptSummry"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', CollateralAccount3, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', CollateralAccount3, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@property
	def CollValtn(self):
		return self._CollValtn

	@CollValtn.setter
	def CollValtn(self, value):
		self._CollValtn = value if value is not None else base_types.UninitialisedField(self, 'CollValtn', CollateralValuation13, True)

	@CollValtn.deleter
	def CollValtn(self):
		del self._CollValtn
		self._CollValtn = base_types.UninitialisedField(self, 'CollValtn', CollateralValuation13, True)

	@property
	def RptSummry(self):
		return self._RptSummry

	@RptSummry.setter
	def RptSummry(self, value):
		self._RptSummry = value if value is not None else base_types.UninitialisedField(self, 'RptSummry', Summary3, False)

	@RptSummry.deleter
	def RptSummry(self):
		del self._RptSummry
		self._RptSummry = base_types.UninitialisedField(self, 'RptSummry', Summary3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollValtn', type=CollateralValuation13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptSummry', type=Summary3, min=1, max=1, mutex_group=None, array=False),
	))