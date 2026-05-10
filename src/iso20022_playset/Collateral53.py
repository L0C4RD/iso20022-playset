import base_types
import Summary3
import BlockChainAddressWallet5
import CollateralValuation13
import CollateralAccount3

class Collateral53(base_types._BaseFieldType):

	__slots__ = ["_CollValtn", "_AcctId", "_BlckChainAdrOrWllt", "_RptSummry"]
	@property
	def CollValtn(self):
		return self._CollValtn

	@CollValtn.setter
	def CollValtn(self, value):
		self._CollValtn = value if type(value) != auto else self.make_default("CollValtn")

	@CollValtn.deleter
	def CollValtn(self):
		del self._CollValtn
		self._CollValtn = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def RptSummry(self):
		return self._RptSummry

	@RptSummry.setter
	def RptSummry(self, value):
		self._RptSummry = value if type(value) != auto else self.make_default("RptSummry")

	@RptSummry.deleter
	def RptSummry(self):
		del self._RptSummry
		self._RptSummry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollValtn', type=CollateralValuation13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSummry', type=Summary3, min=1, max=1, mutex_group=None, array=False),
	))

