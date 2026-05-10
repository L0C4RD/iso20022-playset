from . import base_types
from ._GenericIdentification1 import GenericIdentification1
from ._RequestType1Code import RequestType1Code
from ._RequestType2Code import RequestType2Code

class RequestType2Choice(base_types._BaseFieldType):

	__slots__ = ["_Enqry", "_PmtCtrl", "_Prtry"]
	@property
	def Enqry(self):
		return self._Enqry

	@Enqry.setter
	def Enqry(self, value):
		self._Enqry = value if type(value) != base_types.auto else self.make_default("Enqry")

	@Enqry.deleter
	def Enqry(self):
		del self._Enqry
		self._Enqry = None

	@property
	def PmtCtrl(self):
		return self._PmtCtrl

	@PmtCtrl.setter
	def PmtCtrl(self, value):
		self._PmtCtrl = value if type(value) != base_types.auto else self.make_default("PmtCtrl")

	@PmtCtrl.deleter
	def PmtCtrl(self):
		del self._PmtCtrl
		self._PmtCtrl = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Enqry', type=RequestType2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtCtrl', type=RequestType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

