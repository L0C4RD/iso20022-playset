import base_types
import Max35Text
import InvestigationLocationData1

class RelatedInvestigationData1(base_types._BaseFieldType):

	__slots__ = ["_Lctn", "_InvstgtnId"]
	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	@property
	def InvstgtnId(self):
		return self._InvstgtnId

	@InvstgtnId.setter
	def InvstgtnId(self, value):
		self._InvstgtnId = value if type(value) != auto else self.make_default("InvstgtnId")

	@InvstgtnId.deleter
	def InvstgtnId(self):
		del self._InvstgtnId
		self._InvstgtnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lctn', type=InvestigationLocationData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstgtnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

