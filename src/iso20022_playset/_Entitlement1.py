# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashEntitlement1
from . import Max35Text
from . import PartyIdentification2Choice
from . import SecuritiesEntitlement1

class Entitlement1(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnrId", "_CshDstrbtnDtls", "_SctiesDstrbtnDtls"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@property
	def CshDstrbtnDtls(self):
		return self._CshDstrbtnDtls

	@CshDstrbtnDtls.setter
	def CshDstrbtnDtls(self, value):
		self._CshDstrbtnDtls = value if value is not None else base_types.UninitialisedField(self, 'CshDstrbtnDtls', CashEntitlement1, True)

	@CshDstrbtnDtls.deleter
	def CshDstrbtnDtls(self):
		del self._CshDstrbtnDtls
		self._CshDstrbtnDtls = base_types.UninitialisedField(self, 'CshDstrbtnDtls', CashEntitlement1, True)

	@property
	def SctiesDstrbtnDtls(self):
		return self._SctiesDstrbtnDtls

	@SctiesDstrbtnDtls.setter
	def SctiesDstrbtnDtls(self, value):
		self._SctiesDstrbtnDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesDstrbtnDtls', SecuritiesEntitlement1, True)

	@SctiesDstrbtnDtls.deleter
	def SctiesDstrbtnDtls(self):
		del self._SctiesDstrbtnDtls
		self._SctiesDstrbtnDtls = base_types.UninitialisedField(self, 'SctiesDstrbtnDtls', SecuritiesEntitlement1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshDstrbtnDtls', type=CashEntitlement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesDstrbtnDtls', type=SecuritiesEntitlement1, min=0, max=None, mutex_group=None, array=True),
	))