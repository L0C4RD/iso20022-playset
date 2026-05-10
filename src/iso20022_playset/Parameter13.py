import base_types
import AlgorithmIdentification26
import Algorithm20Code

class Parameter13(base_types._BaseFieldType):

	__slots__ = ["_MskGnrtrAlgo", "_DgstAlgo"]
	@property
	def MskGnrtrAlgo(self):
		return self._MskGnrtrAlgo

	@MskGnrtrAlgo.setter
	def MskGnrtrAlgo(self, value):
		self._MskGnrtrAlgo = value if type(value) != auto else self.make_default("MskGnrtrAlgo")

	@MskGnrtrAlgo.deleter
	def MskGnrtrAlgo(self):
		del self._MskGnrtrAlgo
		self._MskGnrtrAlgo = None

	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if type(value) != auto else self.make_default("DgstAlgo")

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MskGnrtrAlgo', type=AlgorithmIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm20Code, min=0, max=1, mutex_group=None, array=False),
	))

