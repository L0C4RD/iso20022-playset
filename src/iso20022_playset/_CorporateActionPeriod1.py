# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Period1

class CorporateActionPeriod1(base_types._BaseFieldType):

	__slots__ = ["_ActnPrd", "_BlckgPrd", "_CmplsryPurchsPrd", "_IntrstPrd", "_PricClctnPrd"]
	@property
	def ActnPrd(self):
		return self._ActnPrd

	@ActnPrd.setter
	def ActnPrd(self, value):
		self._ActnPrd = value if value is not None else base_types.UninitialisedField(self, 'ActnPrd', Period1, False)

	@ActnPrd.deleter
	def ActnPrd(self):
		del self._ActnPrd
		self._ActnPrd = base_types.UninitialisedField(self, 'ActnPrd', Period1, False)

	@property
	def BlckgPrd(self):
		return self._BlckgPrd

	@BlckgPrd.setter
	def BlckgPrd(self, value):
		self._BlckgPrd = value if value is not None else base_types.UninitialisedField(self, 'BlckgPrd', Period1, False)

	@BlckgPrd.deleter
	def BlckgPrd(self):
		del self._BlckgPrd
		self._BlckgPrd = base_types.UninitialisedField(self, 'BlckgPrd', Period1, False)

	@property
	def CmplsryPurchsPrd(self):
		return self._CmplsryPurchsPrd

	@CmplsryPurchsPrd.setter
	def CmplsryPurchsPrd(self, value):
		self._CmplsryPurchsPrd = value if value is not None else base_types.UninitialisedField(self, 'CmplsryPurchsPrd', Period1, False)

	@CmplsryPurchsPrd.deleter
	def CmplsryPurchsPrd(self):
		del self._CmplsryPurchsPrd
		self._CmplsryPurchsPrd = base_types.UninitialisedField(self, 'CmplsryPurchsPrd', Period1, False)

	@property
	def IntrstPrd(self):
		return self._IntrstPrd

	@IntrstPrd.setter
	def IntrstPrd(self, value):
		self._IntrstPrd = value if value is not None else base_types.UninitialisedField(self, 'IntrstPrd', Period1, False)

	@IntrstPrd.deleter
	def IntrstPrd(self):
		del self._IntrstPrd
		self._IntrstPrd = base_types.UninitialisedField(self, 'IntrstPrd', Period1, False)

	@property
	def PricClctnPrd(self):
		return self._PricClctnPrd

	@PricClctnPrd.setter
	def PricClctnPrd(self, value):
		self._PricClctnPrd = value if value is not None else base_types.UninitialisedField(self, 'PricClctnPrd', Period1, False)

	@PricClctnPrd.deleter
	def PricClctnPrd(self):
		del self._PricClctnPrd
		self._PricClctnPrd = base_types.UninitialisedField(self, 'PricClctnPrd', Period1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckgPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmplsryPurchsPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
	))