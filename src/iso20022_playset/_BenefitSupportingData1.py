# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class BenefitSupportingData1(base_types._BaseFieldType):

	__slots__ = ["_AdmstrId", "_DcsnRsn", "_PrvdrId", "_SvcTp"]
	@property
	def AdmstrId(self):
		return self._AdmstrId

	@AdmstrId.setter
	def AdmstrId(self, value):
		self._AdmstrId = value if value is not None else base_types.UninitialisedField(self, 'AdmstrId', Max35Text, False)

	@AdmstrId.deleter
	def AdmstrId(self):
		del self._AdmstrId
		self._AdmstrId = base_types.UninitialisedField(self, 'AdmstrId', Max35Text, False)

	@property
	def DcsnRsn(self):
		return self._DcsnRsn

	@DcsnRsn.setter
	def DcsnRsn(self, value):
		self._DcsnRsn = value if value is not None else base_types.UninitialisedField(self, 'DcsnRsn', Max35Text, False)

	@DcsnRsn.deleter
	def DcsnRsn(self):
		del self._DcsnRsn
		self._DcsnRsn = base_types.UninitialisedField(self, 'DcsnRsn', Max35Text, False)

	@property
	def PrvdrId(self):
		return self._PrvdrId

	@PrvdrId.setter
	def PrvdrId(self, value):
		self._PrvdrId = value if value is not None else base_types.UninitialisedField(self, 'PrvdrId', Max35Text, False)

	@PrvdrId.deleter
	def PrvdrId(self):
		del self._PrvdrId
		self._PrvdrId = base_types.UninitialisedField(self, 'PrvdrId', Max35Text, False)

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if value is not None else base_types.UninitialisedField(self, 'SvcTp', Max35Text, False)

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = base_types.UninitialisedField(self, 'SvcTp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdmstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcsnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))