from . import base_types
from .Number import Number
from .Algorithm14Code import Algorithm14Code

class ATMSecurityConfiguration4(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntrAlgo", "_MaxSgntrs", "_MaxCerts"]
	@property
	def DgtlSgntrAlgo(self):
		return self._DgtlSgntrAlgo

	@DgtlSgntrAlgo.setter
	def DgtlSgntrAlgo(self, value):
		self._DgtlSgntrAlgo = value if type(value) != base_types.auto else self.make_default("DgtlSgntrAlgo")

	@DgtlSgntrAlgo.deleter
	def DgtlSgntrAlgo(self):
		del self._DgtlSgntrAlgo
		self._DgtlSgntrAlgo = None

	@property
	def MaxSgntrs(self):
		return self._MaxSgntrs

	@MaxSgntrs.setter
	def MaxSgntrs(self, value):
		self._MaxSgntrs = value if type(value) != base_types.auto else self.make_default("MaxSgntrs")

	@MaxSgntrs.deleter
	def MaxSgntrs(self):
		del self._MaxSgntrs
		self._MaxSgntrs = None

	@property
	def MaxCerts(self):
		return self._MaxCerts

	@MaxCerts.setter
	def MaxCerts(self, value):
		self._MaxCerts = value if type(value) != base_types.auto else self.make_default("MaxCerts")

	@MaxCerts.deleter
	def MaxCerts(self):
		del self._MaxCerts
		self._MaxCerts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntrAlgo', type=Algorithm14Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MaxSgntrs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxCerts', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

