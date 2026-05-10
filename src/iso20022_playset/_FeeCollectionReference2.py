from . import base_types
from .Max35Text import Max35Text
from .PartyType32Code import PartyType32Code
from .FeeCollectionIdentification1 import FeeCollectionIdentification1

class FeeCollectionReference2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_AssgnrNtty", "_OthrAssgnrNtty"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def AssgnrNtty(self):
		return self._AssgnrNtty

	@AssgnrNtty.setter
	def AssgnrNtty(self, value):
		self._AssgnrNtty = value if type(value) != base_types.auto else self.make_default("AssgnrNtty")

	@AssgnrNtty.deleter
	def AssgnrNtty(self):
		del self._AssgnrNtty
		self._AssgnrNtty = None

	@property
	def OthrAssgnrNtty(self):
		return self._OthrAssgnrNtty

	@OthrAssgnrNtty.setter
	def OthrAssgnrNtty(self, value):
		self._OthrAssgnrNtty = value if type(value) != base_types.auto else self.make_default("OthrAssgnrNtty")

	@OthrAssgnrNtty.deleter
	def OthrAssgnrNtty(self):
		del self._OthrAssgnrNtty
		self._OthrAssgnrNtty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=FeeCollectionIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AssgnrNtty', type=PartyType32Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAssgnrNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

