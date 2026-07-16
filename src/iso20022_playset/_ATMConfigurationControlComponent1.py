# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMActionType1Code
from . import ATMEnvironment7
from . import ATMPropertyComponent1
from . import ISODateTime
from . import Max35Text

class ATMConfigurationControlComponent1(base_types._BaseFieldType):

	__slots__ = ["_ActnReqrd", "_ActvtnDt", "_CfgtnVrsn", "_Envt", "_Prprty"]
	@property
	def ActnReqrd(self):
		return self._ActnReqrd

	@ActnReqrd.setter
	def ActnReqrd(self, value):
		self._ActnReqrd = value if value is not None else base_types.UninitialisedField(self, 'ActnReqrd', ATMActionType1Code, False)

	@ActnReqrd.deleter
	def ActnReqrd(self):
		del self._ActnReqrd
		self._ActnReqrd = base_types.UninitialisedField(self, 'ActnReqrd', ATMActionType1Code, False)

	@property
	def ActvtnDt(self):
		return self._ActvtnDt

	@ActvtnDt.setter
	def ActvtnDt(self, value):
		self._ActvtnDt = value if value is not None else base_types.UninitialisedField(self, 'ActvtnDt', ISODateTime, False)

	@ActvtnDt.deleter
	def ActvtnDt(self):
		del self._ActvtnDt
		self._ActvtnDt = base_types.UninitialisedField(self, 'ActvtnDt', ISODateTime, False)

	@property
	def CfgtnVrsn(self):
		return self._CfgtnVrsn

	@CfgtnVrsn.setter
	def CfgtnVrsn(self, value):
		self._CfgtnVrsn = value if value is not None else base_types.UninitialisedField(self, 'CfgtnVrsn', Max35Text, False)

	@CfgtnVrsn.deleter
	def CfgtnVrsn(self):
		del self._CfgtnVrsn
		self._CfgtnVrsn = base_types.UninitialisedField(self, 'CfgtnVrsn', Max35Text, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', ATMEnvironment7, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', ATMEnvironment7, False)

	@property
	def Prprty(self):
		return self._Prprty

	@Prprty.setter
	def Prprty(self, value):
		self._Prprty = value if value is not None else base_types.UninitialisedField(self, 'Prprty', ATMPropertyComponent1, True)

	@Prprty.deleter
	def Prprty(self):
		del self._Prprty
		self._Prprty = base_types.UninitialisedField(self, 'Prprty', ATMPropertyComponent1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnReqrd', type=ATMActionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CfgtnVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prprty', type=ATMPropertyComponent1, min=0, max=None, mutex_group=None, array=True),
	))