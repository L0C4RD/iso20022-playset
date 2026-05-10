import base_types
import ResolutionOfInvestigationV13

class CAMT_029_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RsltnOfInvstgtn"]
		@property
		def RsltnOfInvstgtn(self):
			return self._RsltnOfInvstgtn

		@RsltnOfInvstgtn.setter
		def RsltnOfInvstgtn(self, value):
			self._RsltnOfInvstgtn = value if type(value) != auto else self.make_default("RsltnOfInvstgtn")

		@RsltnOfInvstgtn.deleter
		def RsltnOfInvstgtn(self):
			del self._RsltnOfInvstgtn
			self._RsltnOfInvstgtn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RsltnOfInvstgtn', type=ResolutionOfInvestigationV13, min=1, max=1, mutex_group=None, array=False),
		))

