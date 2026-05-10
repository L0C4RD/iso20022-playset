from . import base_types
from .GenericIdentification36 import GenericIdentification36
from .Max350Text import Max350Text
from .RejectedReason33Choice import RejectedReason33Choice

class AdditionalInformation25(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_Qry", "_QryRsn", "_RjctnRsn"]
	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	@property
	def Qry(self):
		return self._Qry

	@Qry.setter
	def Qry(self, value):
		self._Qry = value if type(value) != auto else self.make_default("Qry")

	@Qry.deleter
	def Qry(self):
		del self._Qry
		self._Qry = None

	@property
	def QryRsn(self):
		return self._QryRsn

	@QryRsn.setter
	def QryRsn(self, value):
		self._QryRsn = value if type(value) != auto else self.make_default("QryRsn")

	@QryRsn.deleter
	def QryRsn(self):
		del self._QryRsn
		self._QryRsn = None

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=GenericIdentification36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qry', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectedReason33Choice, min=0, max=1, mutex_group=None, array=False),
	))

