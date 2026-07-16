# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationInformation5
from . import Max140Text
from . import Max35Text

class IdentificationModification5(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Id", "_OrgnlPtyAndAcctId", "_UpdtdPtyAndAcctId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def OrgnlPtyAndAcctId(self):
		return self._OrgnlPtyAndAcctId

	@OrgnlPtyAndAcctId.setter
	def OrgnlPtyAndAcctId(self, value):
		self._OrgnlPtyAndAcctId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPtyAndAcctId', IdentificationInformation5, False)

	@OrgnlPtyAndAcctId.deleter
	def OrgnlPtyAndAcctId(self):
		del self._OrgnlPtyAndAcctId
		self._OrgnlPtyAndAcctId = base_types.UninitialisedField(self, 'OrgnlPtyAndAcctId', IdentificationInformation5, False)

	@property
	def UpdtdPtyAndAcctId(self):
		return self._UpdtdPtyAndAcctId

	@UpdtdPtyAndAcctId.setter
	def UpdtdPtyAndAcctId(self, value):
		self._UpdtdPtyAndAcctId = value if value is not None else base_types.UninitialisedField(self, 'UpdtdPtyAndAcctId', IdentificationInformation5, False)

	@UpdtdPtyAndAcctId.deleter
	def UpdtdPtyAndAcctId(self):
		del self._UpdtdPtyAndAcctId
		self._UpdtdPtyAndAcctId = base_types.UninitialisedField(self, 'UpdtdPtyAndAcctId', IdentificationInformation5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPtyAndAcctId', type=IdentificationInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdtdPtyAndAcctId', type=IdentificationInformation5, min=1, max=1, mutex_group=None, array=False),
	))