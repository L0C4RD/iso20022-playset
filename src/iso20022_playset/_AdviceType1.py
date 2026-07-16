# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdviceType1Choice

class AdviceType1(base_types._BaseFieldType):

	__slots__ = ["_CdtAdvc", "_DbtAdvc"]
	@property
	def CdtAdvc(self):
		return self._CdtAdvc

	@CdtAdvc.setter
	def CdtAdvc(self, value):
		self._CdtAdvc = value if value is not None else base_types.UninitialisedField(self, 'CdtAdvc', AdviceType1Choice, False)

	@CdtAdvc.deleter
	def CdtAdvc(self):
		del self._CdtAdvc
		self._CdtAdvc = base_types.UninitialisedField(self, 'CdtAdvc', AdviceType1Choice, False)

	@property
	def DbtAdvc(self):
		return self._DbtAdvc

	@DbtAdvc.setter
	def DbtAdvc(self, value):
		self._DbtAdvc = value if value is not None else base_types.UninitialisedField(self, 'DbtAdvc', AdviceType1Choice, False)

	@DbtAdvc.deleter
	def DbtAdvc(self):
		del self._DbtAdvc
		self._DbtAdvc = base_types.UninitialisedField(self, 'DbtAdvc', AdviceType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtAdvc', type=AdviceType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtAdvc', type=AdviceType1Choice, min=0, max=1, mutex_group=None, array=False),
	))