# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification38Choice
from . import InvoiceTotals7
from . import ServiceCategoryTotals7

class InvoiceTotals8(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_InvcTtls", "_SvcCtgyTtls"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentification38Choice, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentification38Choice, False)

	@property
	def InvcTtls(self):
		return self._InvcTtls

	@InvcTtls.setter
	def InvcTtls(self, value):
		self._InvcTtls = value if value is not None else base_types.UninitialisedField(self, 'InvcTtls', InvoiceTotals7, False)

	@InvcTtls.deleter
	def InvcTtls(self):
		del self._InvcTtls
		self._InvcTtls = base_types.UninitialisedField(self, 'InvcTtls', InvoiceTotals7, False)

	@property
	def SvcCtgyTtls(self):
		return self._SvcCtgyTtls

	@SvcCtgyTtls.setter
	def SvcCtgyTtls(self, value):
		self._SvcCtgyTtls = value if value is not None else base_types.UninitialisedField(self, 'SvcCtgyTtls', ServiceCategoryTotals7, True)

	@SvcCtgyTtls.deleter
	def SvcCtgyTtls(self):
		del self._SvcCtgyTtls
		self._SvcCtgyTtls = base_types.UninitialisedField(self, 'SvcCtgyTtls', ServiceCategoryTotals7, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification38Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcTtls', type=InvoiceTotals7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCtgyTtls', type=ServiceCategoryTotals7, min=1, max=None, mutex_group=None, array=True),
	))