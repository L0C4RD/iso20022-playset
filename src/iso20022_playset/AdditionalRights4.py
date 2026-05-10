from . import base_types
from .AdditionalRightCode1Choice import AdditionalRightCode1Choice
from .DateFormat58Choice import DateFormat58Choice
from .Max2048Text import Max2048Text
from .AdditionalRightThreshold2Choice import AdditionalRightThreshold2Choice

class AdditionalRights4(base_types._BaseFieldType):

	__slots__ = ["_AddtlRghtInfURLAdr", "_AddtlRghtDdln", "_AddtlRght", "_AddtlRghtMktDdln", "_AddtlRghtThrshld"]
	@property
	def AddtlRghtInfURLAdr(self):
		return self._AddtlRghtInfURLAdr

	@AddtlRghtInfURLAdr.setter
	def AddtlRghtInfURLAdr(self, value):
		self._AddtlRghtInfURLAdr = value if type(value) != base_types.auto else self.make_default("AddtlRghtInfURLAdr")

	@AddtlRghtInfURLAdr.deleter
	def AddtlRghtInfURLAdr(self):
		del self._AddtlRghtInfURLAdr
		self._AddtlRghtInfURLAdr = None

	@property
	def AddtlRghtDdln(self):
		return self._AddtlRghtDdln

	@AddtlRghtDdln.setter
	def AddtlRghtDdln(self, value):
		self._AddtlRghtDdln = value if type(value) != base_types.auto else self.make_default("AddtlRghtDdln")

	@AddtlRghtDdln.deleter
	def AddtlRghtDdln(self):
		del self._AddtlRghtDdln
		self._AddtlRghtDdln = None

	@property
	def AddtlRght(self):
		return self._AddtlRght

	@AddtlRght.setter
	def AddtlRght(self, value):
		self._AddtlRght = value if type(value) != base_types.auto else self.make_default("AddtlRght")

	@AddtlRght.deleter
	def AddtlRght(self):
		del self._AddtlRght
		self._AddtlRght = None

	@property
	def AddtlRghtMktDdln(self):
		return self._AddtlRghtMktDdln

	@AddtlRghtMktDdln.setter
	def AddtlRghtMktDdln(self, value):
		self._AddtlRghtMktDdln = value if type(value) != base_types.auto else self.make_default("AddtlRghtMktDdln")

	@AddtlRghtMktDdln.deleter
	def AddtlRghtMktDdln(self):
		del self._AddtlRghtMktDdln
		self._AddtlRghtMktDdln = None

	@property
	def AddtlRghtThrshld(self):
		return self._AddtlRghtThrshld

	@AddtlRghtThrshld.setter
	def AddtlRghtThrshld(self, value):
		self._AddtlRghtThrshld = value if type(value) != base_types.auto else self.make_default("AddtlRghtThrshld")

	@AddtlRghtThrshld.deleter
	def AddtlRghtThrshld(self):
		del self._AddtlRghtThrshld
		self._AddtlRghtThrshld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRghtInfURLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRghtDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRght', type=AdditionalRightCode1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRghtMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRghtThrshld', type=AdditionalRightThreshold2Choice, min=0, max=1, mutex_group=None, array=False),
	))

