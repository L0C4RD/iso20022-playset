# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMEnvironment7
from . import ATMVersionReport1
from . import Max35Text

class ATMConfigurationReportComponent1(base_types._BaseFieldType):

	__slots__ = ["_ActvVrsn", "_Envt", "_NonActvVrsn"]
	@property
	def ActvVrsn(self):
		return self._ActvVrsn

	@ActvVrsn.setter
	def ActvVrsn(self, value):
		self._ActvVrsn = value if value is not None else base_types.UninitialisedField(self, 'ActvVrsn', Max35Text, False)

	@ActvVrsn.deleter
	def ActvVrsn(self):
		del self._ActvVrsn
		self._ActvVrsn = base_types.UninitialisedField(self, 'ActvVrsn', Max35Text, False)

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
	def NonActvVrsn(self):
		return self._NonActvVrsn

	@NonActvVrsn.setter
	def NonActvVrsn(self, value):
		self._NonActvVrsn = value if value is not None else base_types.UninitialisedField(self, 'NonActvVrsn', ATMVersionReport1, True)

	@NonActvVrsn.deleter
	def NonActvVrsn(self):
		del self._NonActvVrsn
		self._NonActvVrsn = base_types.UninitialisedField(self, 'NonActvVrsn', ATMVersionReport1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonActvVrsn', type=ATMVersionReport1, min=0, max=None, mutex_group=None, array=True),
	))