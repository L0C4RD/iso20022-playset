# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text

class BenefitSupportingData1(base_types._BaseFieldType):

	__slots__ = ["_AdmstrId", "_DcsnRsn", "_PrvdrId", "_SvcTp"]
	@property
	def AdmstrId(self):
		return self._AdmstrId

	@AdmstrId.setter
	def AdmstrId(self, value):
		self._AdmstrId = value if type(value) != base_types.auto else self.make_default("AdmstrId")

	@AdmstrId.deleter
	def AdmstrId(self):
		del self._AdmstrId
		self._AdmstrId = None

	@property
	def DcsnRsn(self):
		return self._DcsnRsn

	@DcsnRsn.setter
	def DcsnRsn(self, value):
		self._DcsnRsn = value if type(value) != base_types.auto else self.make_default("DcsnRsn")

	@DcsnRsn.deleter
	def DcsnRsn(self):
		del self._DcsnRsn
		self._DcsnRsn = None

	@property
	def PrvdrId(self):
		return self._PrvdrId

	@PrvdrId.setter
	def PrvdrId(self, value):
		self._PrvdrId = value if type(value) != base_types.auto else self.make_default("PrvdrId")

	@PrvdrId.deleter
	def PrvdrId(self):
		del self._PrvdrId
		self._PrvdrId = None

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != base_types.auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdmstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcsnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))