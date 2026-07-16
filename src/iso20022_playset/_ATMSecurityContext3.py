# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMEquipment3
from . import ATMSecurityConfiguration1
from . import ATMSecurityScheme3Code

class ATMSecurityContext3(base_types._BaseFieldType):

	__slots__ = ["_CurCfgtn", "_CurSctySchme", "_DvcPrprty"]
	@property
	def CurCfgtn(self):
		return self._CurCfgtn

	@CurCfgtn.setter
	def CurCfgtn(self, value):
		self._CurCfgtn = value if value is not None else base_types.UninitialisedField(self, 'CurCfgtn', ATMSecurityConfiguration1, False)

	@CurCfgtn.deleter
	def CurCfgtn(self):
		del self._CurCfgtn
		self._CurCfgtn = base_types.UninitialisedField(self, 'CurCfgtn', ATMSecurityConfiguration1, False)

	@property
	def CurSctySchme(self):
		return self._CurSctySchme

	@CurSctySchme.setter
	def CurSctySchme(self, value):
		self._CurSctySchme = value if value is not None else base_types.UninitialisedField(self, 'CurSctySchme', ATMSecurityScheme3Code, False)

	@CurSctySchme.deleter
	def CurSctySchme(self):
		del self._CurSctySchme
		self._CurSctySchme = base_types.UninitialisedField(self, 'CurSctySchme', ATMSecurityScheme3Code, False)

	@property
	def DvcPrprty(self):
		return self._DvcPrprty

	@DvcPrprty.setter
	def DvcPrprty(self, value):
		self._DvcPrprty = value if value is not None else base_types.UninitialisedField(self, 'DvcPrprty', ATMEquipment3, False)

	@DvcPrprty.deleter
	def DvcPrprty(self):
		del self._DvcPrprty
		self._DvcPrprty = base_types.UninitialisedField(self, 'DvcPrprty', ATMEquipment3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurCfgtn', type=ATMSecurityConfiguration1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurSctySchme', type=ATMSecurityScheme3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcPrprty', type=ATMEquipment3, min=0, max=1, mutex_group=None, array=False),
	))