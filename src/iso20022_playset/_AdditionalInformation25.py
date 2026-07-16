# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification36
from . import Max350Text
from . import RejectedReason33Choice

class AdditionalInformation25(base_types._BaseFieldType):

	__slots__ = ["_Qry", "_QryRsn", "_QryTp", "_RjctnRsn"]
	@property
	def Qry(self):
		return self._Qry

	@Qry.setter
	def Qry(self, value):
		self._Qry = value if value is not None else base_types.UninitialisedField(self, 'Qry', Max350Text, False)

	@Qry.deleter
	def Qry(self):
		del self._Qry
		self._Qry = base_types.UninitialisedField(self, 'Qry', Max350Text, False)

	@property
	def QryRsn(self):
		return self._QryRsn

	@QryRsn.setter
	def QryRsn(self, value):
		self._QryRsn = value if value is not None else base_types.UninitialisedField(self, 'QryRsn', Max350Text, False)

	@QryRsn.deleter
	def QryRsn(self):
		del self._QryRsn
		self._QryRsn = base_types.UninitialisedField(self, 'QryRsn', Max350Text, False)

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if value is not None else base_types.UninitialisedField(self, 'QryTp', GenericIdentification36, False)

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = base_types.UninitialisedField(self, 'QryTp', GenericIdentification36, False)

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', RejectedReason33Choice, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', RejectedReason33Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qry', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=GenericIdentification36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectedReason33Choice, min=0, max=1, mutex_group=None, array=False),
	))