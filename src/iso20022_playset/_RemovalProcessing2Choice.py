# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import GenericIdentification37
from . import SecurityIdentification19

class RemovalProcessing2Choice(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_IndxId", "_IssrCtry"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def IndxId(self):
		return self._IndxId

	@IndxId.setter
	def IndxId(self, value):
		self._IndxId = value if value is not None else base_types.UninitialisedField(self, 'IndxId', GenericIdentification37, False)

	@IndxId.deleter
	def IndxId(self):
		del self._IndxId
		self._IndxId = base_types.UninitialisedField(self, 'IndxId', GenericIdentification37, False)

	@property
	def IssrCtry(self):
		return self._IssrCtry

	@IssrCtry.setter
	def IssrCtry(self, value):
		self._IssrCtry = value if value is not None else base_types.UninitialisedField(self, 'IssrCtry', CountryCode, False)

	@IssrCtry.deleter
	def IssrCtry(self):
		del self._IssrCtry
		self._IssrCtry = base_types.UninitialisedField(self, 'IssrCtry', CountryCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxId', type=GenericIdentification37, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IssrCtry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
	))