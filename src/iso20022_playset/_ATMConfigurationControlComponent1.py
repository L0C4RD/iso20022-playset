from . import base_types
from ._ATMEnvironment7 import ATMEnvironment7
from ._Max35Text import Max35Text
from ._ATMActionType1Code import ATMActionType1Code
from ._ATMPropertyComponent1 import ATMPropertyComponent1
from ._ISODateTime import ISODateTime

class ATMConfigurationControlComponent1(base_types._BaseFieldType):

	__slots__ = ["_CfgtnVrsn", "_ActnReqrd", "_Prprty", "_Envt", "_ActvtnDt"]
	@property
	def CfgtnVrsn(self):
		return self._CfgtnVrsn

	@CfgtnVrsn.setter
	def CfgtnVrsn(self, value):
		self._CfgtnVrsn = value if type(value) != base_types.auto else self.make_default("CfgtnVrsn")

	@CfgtnVrsn.deleter
	def CfgtnVrsn(self):
		del self._CfgtnVrsn
		self._CfgtnVrsn = None

	@property
	def ActnReqrd(self):
		return self._ActnReqrd

	@ActnReqrd.setter
	def ActnReqrd(self, value):
		self._ActnReqrd = value if type(value) != base_types.auto else self.make_default("ActnReqrd")

	@ActnReqrd.deleter
	def ActnReqrd(self):
		del self._ActnReqrd
		self._ActnReqrd = None

	@property
	def Prprty(self):
		return self._Prprty

	@Prprty.setter
	def Prprty(self, value):
		self._Prprty = value if type(value) != base_types.auto else self.make_default("Prprty")

	@Prprty.deleter
	def Prprty(self):
		del self._Prprty
		self._Prprty = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def ActvtnDt(self):
		return self._ActvtnDt

	@ActvtnDt.setter
	def ActvtnDt(self, value):
		self._ActvtnDt = value if type(value) != base_types.auto else self.make_default("ActvtnDt")

	@ActvtnDt.deleter
	def ActvtnDt(self):
		del self._ActvtnDt
		self._ActvtnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CfgtnVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnReqrd', type=ATMActionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prprty', type=ATMPropertyComponent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

