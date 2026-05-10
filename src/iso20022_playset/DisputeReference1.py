from . import base_types
import PartyType32Code
import DisputeIdentification1
import Max35Text

class DisputeReference1(base_types._BaseFieldType):

	__slots__ = ["_DsptId", "_AssgnrNtty", "_OthrAssgnrNtty"]
	@property
	def DsptId(self):
		return self._DsptId

	@DsptId.setter
	def DsptId(self, value):
		self._DsptId = value if type(value) != auto else self.make_default("DsptId")

	@DsptId.deleter
	def DsptId(self):
		del self._DsptId
		self._DsptId = None

	@property
	def AssgnrNtty(self):
		return self._AssgnrNtty

	@AssgnrNtty.setter
	def AssgnrNtty(self, value):
		self._AssgnrNtty = value if type(value) != auto else self.make_default("AssgnrNtty")

	@AssgnrNtty.deleter
	def AssgnrNtty(self):
		del self._AssgnrNtty
		self._AssgnrNtty = None

	@property
	def OthrAssgnrNtty(self):
		return self._OthrAssgnrNtty

	@OthrAssgnrNtty.setter
	def OthrAssgnrNtty(self, value):
		self._OthrAssgnrNtty = value if type(value) != auto else self.make_default("OthrAssgnrNtty")

	@OthrAssgnrNtty.deleter
	def OthrAssgnrNtty(self):
		del self._OthrAssgnrNtty
		self._OthrAssgnrNtty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsptId', type=DisputeIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AssgnrNtty', type=PartyType32Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAssgnrNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

