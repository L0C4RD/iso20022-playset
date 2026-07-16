# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMService12
from . import Max35Text

class ATMContext11(base_types._BaseFieldType):

	__slots__ = ["_SsnRef", "_Svc"]
	@property
	def SsnRef(self):
		return self._SsnRef

	@SsnRef.setter
	def SsnRef(self, value):
		self._SsnRef = value if value is not None else base_types.UninitialisedField(self, 'SsnRef', Max35Text, False)

	@SsnRef.deleter
	def SsnRef(self):
		del self._SsnRef
		self._SsnRef = base_types.UninitialisedField(self, 'SsnRef', Max35Text, False)

	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if value is not None else base_types.UninitialisedField(self, 'Svc', ATMService12, False)

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = base_types.UninitialisedField(self, 'Svc', ATMService12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SsnRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=ATMService12, min=0, max=1, mutex_group=None, array=False),
	))