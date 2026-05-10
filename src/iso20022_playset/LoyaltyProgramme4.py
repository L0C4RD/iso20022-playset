import base_types
import Max70Text
import Max35Text

class LoyaltyProgramme4(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Tp", "_PtcptId"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def PtcptId(self):
		return self._PtcptId

	@PtcptId.setter
	def PtcptId(self, value):
		self._PtcptId = value if type(value) != auto else self.make_default("PtcptId")

	@PtcptId.deleter
	def PtcptId(self):
		del self._PtcptId
		self._PtcptId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtcptId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

