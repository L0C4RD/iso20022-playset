# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentificationAndName7
from . import AnyBICDec2014Identifier
from . import Max35Text

class CashAccount206(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctTpDesc", "_Svcr"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentificationAndName7, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentificationAndName7, False)

	@property
	def AcctTpDesc(self):
		return self._AcctTpDesc

	@AcctTpDesc.setter
	def AcctTpDesc(self, value):
		self._AcctTpDesc = value if value is not None else base_types.UninitialisedField(self, 'AcctTpDesc', Max35Text, False)

	@AcctTpDesc.deleter
	def AcctTpDesc(self):
		del self._AcctTpDesc
		self._AcctTpDesc = base_types.UninitialisedField(self, 'AcctTpDesc', Max35Text, False)

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if value is not None else base_types.UninitialisedField(self, 'Svcr', AnyBICDec2014Identifier, False)

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = base_types.UninitialisedField(self, 'Svcr', AnyBICDec2014Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentificationAndName7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTpDesc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
	))