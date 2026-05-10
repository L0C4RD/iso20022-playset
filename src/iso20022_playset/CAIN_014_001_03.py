import base_types
import RetrievalFulfilmentInitiationV03

class CAIN_014_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrvlFlfmtInitn"]
		@property
		def RtrvlFlfmtInitn(self):
			return self._RtrvlFlfmtInitn

		@RtrvlFlfmtInitn.setter
		def RtrvlFlfmtInitn(self, value):
			self._RtrvlFlfmtInitn = value if type(value) != auto else self.make_default("RtrvlFlfmtInitn")

		@RtrvlFlfmtInitn.deleter
		def RtrvlFlfmtInitn(self):
			del self._RtrvlFlfmtInitn
			self._RtrvlFlfmtInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrvlFlfmtInitn', type=RetrievalFulfilmentInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))

