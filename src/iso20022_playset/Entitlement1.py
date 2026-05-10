import base_types
import Max35Text
import CashEntitlement1
import PartyIdentification2Choice
import SecuritiesEntitlement1

class Entitlement1(base_types._BaseFieldType):

	__slots__ = ["_CshDstrbtnDtls", "_AcctId", "_SctiesDstrbtnDtls", "_AcctOwnrId"]
	@property
	def CshDstrbtnDtls(self):
		return self._CshDstrbtnDtls

	@CshDstrbtnDtls.setter
	def CshDstrbtnDtls(self, value):
		self._CshDstrbtnDtls = value if type(value) != auto else self.make_default("CshDstrbtnDtls")

	@CshDstrbtnDtls.deleter
	def CshDstrbtnDtls(self):
		del self._CshDstrbtnDtls
		self._CshDstrbtnDtls = None

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
	def SctiesDstrbtnDtls(self):
		return self._SctiesDstrbtnDtls

	@SctiesDstrbtnDtls.setter
	def SctiesDstrbtnDtls(self, value):
		self._SctiesDstrbtnDtls = value if type(value) != auto else self.make_default("SctiesDstrbtnDtls")

	@SctiesDstrbtnDtls.deleter
	def SctiesDstrbtnDtls(self):
		del self._SctiesDstrbtnDtls
		self._SctiesDstrbtnDtls = None

	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if type(value) != auto else self.make_default("AcctOwnrId")

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshDstrbtnDtls', type=CashEntitlement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesDstrbtnDtls', type=SecuritiesEntitlement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))

